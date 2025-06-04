import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GLib
import configparser
import os
import subprocess
import threading
from datetime import datetime
import signal

CONFIG_FILE = "blender-render-background.ini"

class App(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.blender-render-background",
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)
        self.render_process = None
        self.start_time = None
        self.is_rendering = False
        self.render_thread = None

    def on_activate(self, app):
        self.janela = Gtk.ApplicationWindow(application=app)
        self.janela.set_title("Blender Render Background V2 Beta")
        self.janela.set_default_size(650, 300)
        self.janela.set_resizable(False)
        self.janela.set_border_width(20)

        # Verifique se o ícone existe antes de tentar defini-lo
        if os.path.exists("icons/blender-icon.png"):
            self.janela.set_icon_from_file("icons/blender-icon.png")

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.janela.add(main_box)

        # Seção de Configuração
        config_frame = Gtk.Frame(label="Path do Blender")
        config_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        config_frame.add(config_box)
        main_box.pack_start(config_frame, False, False, 0)

        # Blender Executável
        blender_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.file_chooser_blender = Gtk.FileChooserButton.new(
            "Selecione o Blender", Gtk.FileChooserAction.OPEN)
        self.file_chooser_blender.connect("file-set", self.on_blender_file_set)

        self.entry_blender_path = Gtk.Entry()
        self.entry_blender_path.set_editable(False)
        self.entry_blender_path.set_hexpand(True)

        blender_box.pack_start(self.file_chooser_blender, True, True, 0)
        blender_box.pack_start(self.entry_blender_path, True, True, 0)
        config_box.pack_start(blender_box, False, False, 0)

        # Seleciona o Arquivo .blend para Renderizar
        blend_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl_blend = Gtk.Label(label="Arquivo (.blend) ")
        lbl_blend.set_halign(Gtk.Align.START)
        blend_box.pack_start(lbl_blend, False, False, 0)

        self.file_chooser_blend = Gtk.FileChooserButton.new(
            "Selecione o arquivo .blend", Gtk.FileChooserAction.OPEN)
        self.file_chooser_blend.set_current_folder(os.path.expanduser("~"))
        filter_blend = Gtk.FileFilter()
        filter_blend.set_name("Arquivo Blend")
        filter_blend.add_pattern("*.blend")
        self.file_chooser_blend.add_filter(filter_blend)
        blend_box.pack_start(self.file_chooser_blend, True, True, 0)
        config_box.pack_start(blend_box, False, False, 0)

        # Botões de Renderização e Cancelar
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.btn_render = Gtk.Button(label="Iniciar Renderização")
        self.btn_render.connect("clicked", self.on_renderizar)

        self.btn_cancel = Gtk.Button(label="Cancelar")
        self.btn_cancel.connect("clicked", self.on_cancelar)
        self.btn_cancel.set_sensitive(False)

        button_box.pack_start(self.btn_render, True, True, 0)
        button_box.pack_start(self.btn_cancel, True, True, 0)
        config_box.pack_start(button_box, False, False, 10)

        # Seção de Status
        status_frame = Gtk.Frame(label="")
        status_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        status_frame.add(status_box)
        main_box.pack_start(status_frame, False, False, 0)

        self.lbl_pid = Gtk.Label(label="Process ID:...")
        self.lbl_pid.set_halign(Gtk.Align.START)
        status_box.pack_start(self.lbl_pid, False, False, 0)

        self.lbl_tempo = Gtk.Label(label="Tempo decorrido:...")
        self.lbl_tempo.set_halign(Gtk.Align.START)
        status_box.pack_start(self.lbl_tempo, False, False, 0)

        self.lbl_progresso = Gtk.Label(label="Progresso: Aguardando Início...")
        self.lbl_progresso.set_halign(Gtk.Align.START)
        status_box.pack_start(self.lbl_progresso, False, False, 0)

        # Footer
        footer_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        lbl_footer = Gtk.Label(label="Donate Paypal: Sergio ReOli (sergioreoli@hotmail.com)")
        lbl_footer.set_halign(Gtk.Align.START)
        footer_box.pack_start(lbl_footer, False, False, 0)
        main_box.pack_end(footer_box, False, False, 0)

        self.janela.show_all()

        GLib.timeout_add(100, self.carregar_config)
        GLib.timeout_add(150, self.centralizar_janela)
        GLib.timeout_add(1000, self.atualizar_tempo)

    def centralizar_janela(self):
        screen = self.janela.get_screen()
        monitor = screen.get_primary_monitor()
        geometry = screen.get_monitor_geometry(monitor)

        width = self.janela.get_allocated_width()
        height = self.janela.get_allocated_height()

        pos_x = geometry.x + (geometry.width - width) // 2
        pos_y = geometry.y + (geometry.height - height) // 2

        self.janela.move(pos_x, pos_y)
        return False

    def atualizar_tempo(self):
        if self.is_rendering and self.start_time:
            tempo_decorrido = datetime.now() - self.start_time
            horas, resto = divmod(tempo_decorrido.total_seconds(), 3600)
            minutos, segundos = divmod(resto, 60)
            self.lbl_tempo.set_text(
                f"Tempo decorrido: {int(horas):02d}:{int(minutos):02d}:{int(segundos):02d}"
            )
        return True

    def on_blender_file_set(self, widget):
        caminho = widget.get_filename()
        if caminho:
            self.entry_blender_path.set_text(caminho)

    def carregar_config(self):
        config = configparser.ConfigParser()
        if os.path.exists(CONFIG_FILE):
            try:
                config.read(CONFIG_FILE)
                blender_path = config.get('DEFAULT', 'blender_path', fallback=None)
                if blender_path and os.path.exists(blender_path):
                    self.file_chooser_blender.set_filename(blender_path)
                    self.entry_blender_path.set_text(blender_path)
            except Exception as e:
                print("Erro ao carregar configuração:", e)
        return False

    def salvar_config(self):
        try:
            config = configparser.ConfigParser()
            config['DEFAULT'] = {'blender_path': self.file_chooser_blender.get_filename() or ""}
            with open(CONFIG_FILE, 'w') as configfile:
                config.write(configfile)
        except Exception as e:
            print("Erro ao salvar configuração:", e)

    def on_cancelar(self, button):
        if self.render_process and self.is_rendering:
            try:
                self.render_process.terminate()
                self.is_rendering = False
                self.btn_cancel.set_sensitive(False)
                self.lbl_progresso.set_text("Progresso: Renderização cancelada")
                self.mostrar_mensagem("Renderização Cancelada", "A renderização foi cancelada pelo usuário.")
                self.restaurar_interface()
            except Exception as e:
                print(f"Erro ao cancelar a renderização: {str(e)}")

    def mostrar_mensagem(self, titulo, mensagem):
        dialog = Gtk.MessageDialog(
            transient_for=self.janela,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text=titulo
        )
        dialog.format_secondary_text(mensagem)
        dialog.run()
        dialog.destroy()

    def mostrar_erro(self, titulo, mensagem):
        dialog = Gtk.MessageDialog(
            transient_for=self.janela,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=titulo
        )
        dialog.format_secondary_text(mensagem)
        dialog.run()
        dialog.destroy()

    def restaurar_interface(self):
        self.btn_render.set_label("Iniciar Renderização")
        self.btn_render.set_sensitive(True)
        self.file_chooser_blend.set_sensitive(True)
        self.file_chooser_blender.set_sensitive(True)
        self.lbl_pid.set_text("PID:...")

    def monitorar_progresso(self):
        try:
            while self.is_rendering:
                line = self.render_process.stdout.readline()
                if not line and self.render_process.poll() is not None:
                    break

                if "Fra:" in line:
                    frame_info = line.split("Fra:")[1].split("|")[0].strip()
                    GLib.idle_add(self.lbl_progresso.set_text, f"Frame: {frame_info}")

            if self.is_rendering:
                self.is_rendering = False
                GLib.idle_add(self.finalizar_renderizacao)
        except Exception as e:
            print(f"Erro ao monitorar progresso: {str(e)}")

    def finalizar_renderizacao(self):
        tempo_total = datetime.now() - self.start_time
        horas, resto = divmod(tempo_total.total_seconds(), 3600)
        minutos, segundos = divmod(resto, 60)

        self.mostrar_mensagem(
            "Renderização Concluída",
            f"Tempo total: {int(horas):02d}h {int(minutos):02d}m {int(segundos):02d}s\n"
            f"Arquivo renderizado: {os.path.basename(self.file_chooser_blend.get_filename())}"
        )
        self.restaurar_interface()

    def on_renderizar(self, button):
        if self.is_rendering:
            return

        blender = self.file_chooser_blender.get_filename()
        arquivo = self.file_chooser_blend.get_filename()

        if not blender or not arquivo:
            self.mostrar_erro("Configuração Incompleta",
                            "Selecione o executável do Blender e um arquivo .blend")
            return

        try:
            self.preparar_renderizacao(blender, arquivo)
            self.render_thread = threading.Thread(target=self.monitorar_progresso, daemon=True)
            self.render_thread.start()
        except Exception as e:
            self.is_rendering = False
            self.mostrar_erro("Erro ao Iniciar Renderização", f"Detalhes: {str(e)}")

    def preparar_renderizacao(self, blender, arquivo):
        try:
            self.start_time = datetime.now()
            self.is_rendering = True

            self.render_process = subprocess.Popen(
                [blender, "-b", arquivo, "-a"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                bufsize=1
            )

            self.btn_render.set_label("Renderizando...")
            self.btn_render.set_sensitive(False)
            self.btn_cancel.set_sensitive(True)
            self.file_chooser_blend.set_sensitive(False)
            self.file_chooser_blender.set_sensitive(False)
            self.lbl_pid.set_text(f"PID: {self.render_process.pid}")
            self.lbl_progresso.set_text("Progresso: Iniciando...")

            self.salvar_config()
        except Exception as e:
            self.is_rendering = False
            self.mostrar_erro("Erro ao Preparar Renderização", f"Detalhes: {str(e)}")

app = App()
app.run(None)

