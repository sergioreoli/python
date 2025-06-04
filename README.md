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

## 🚀 Como usar

```bash
sudo apt install python3-gi gir1.2-gtk-3.0


...bash

