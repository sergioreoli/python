# Blender Render Background V2 (GTK GUI)

Aplicativo em Python + GTK para facilitar a renderização de arquivos `.blend` em segundo plano (modo background) com o Blender.

![screenshot](docs/screenshot.png) <!-- opcional se quiser colocar uma imagem -->

---

c✨ Recursos

- Interface gráfica leve e direta usando GTK+3
- Seleção do executável do Blender via FileChooser
- Suporte à seleção de arquivos `.blend`
- Execução em segundo plano via terminal (`-b -a`)
- Monitoramento do progresso em tempo real
- Informações de tempo decorrido e PID do processo
- Cancelamento da renderização
- Salvamento automático do caminho do Blender em `.ini`

---

## 🔧 Requisitos

- Python 3.x
- [PyGObject (GTK+3)](https://pygobject.readthedocs.io/en/latest/)
- Blender instalado no sistema

Instale o PyGObject (no Linux):

<code>
sudo apt install python3-gi gir1.2-gtk-3.0
</code>


## 🚀 Como usar
Clone o repositório:

<code>
git clone https://github.com/SEU_USUARIO/blender-render-background.git
cd blender-render-background
</code>

## Execute o programa:

<code>
python3 bldender-render-background.py
</code>  

## Selecione:

O executável do Blender
O arquivo .blend desejado
Clique em "Iniciar Renderização"

##💡 Observações
O caminho do Blender é salvo automaticamente no arquivo blender-render-background.ini

A renderização é feita em background usando subprocess.Popen()

## 📤 Licença
MIT License. Veja o arquivo LICENSE para mais detalhes.

## Doação
Se esse app te ajudou, considere apoiar com uma doação:
Paypal: sergioreoli@hotmail.com

