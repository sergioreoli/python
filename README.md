# Blender Render Background V2 (GTK GUI)

<img alt="blender-render-background-screenshot.png" src="blender-render-background-screenshot.png?raw=true" data-hpc="true" class="Box-sc-g0xbh4-0 fzFXnm">

O Aplicativo em Python + GTK para facilitar a Renderização de arquivos `.blend` em segundo plano (modo background) com o Blender.

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

```
> sudo apt install python3-gi gir1.2-gtk-3.0
```

## 🚀 Como usar
Clone o repositório:

```
git clone https://github.com/sergioreoli/blender-render-background.git
cd blender-render-background
```

## Execute o programa:

```
python3 bldender-render-background.py
```
## Selecione:

O executável do Blender
O arquivo .blend desejado
Clique em "Iniciar Renderização"

##💡 Observações
O caminho do Blender é salvo automaticamente no arquivo blender-render-background.ini

A renderização é feita em background usando subprocess.Popen()


## Doação
Se esse app te ajudou, considere apoiar com uma doação:
Paypal: sergioreoli@hotmail.com

### 📄 `.gitignore`

```
__pycache__/
*.pyc
*.pyo
*.swp
blender-render-background.ini
````

## Estrutura sugerida do repositório

```
blender-render-background/
├── icons/---
> If we pull together and commit ourselves, then we can push through anything.

— Mona the Octocat
│   └── blender-icon.png
├── docs/
│   └── screenshot.png (opcional)
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

## 📤 Licença
```
MIT License

Copyright (c) 2025 Sergio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.

```

