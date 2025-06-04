# Blender Render Background V2 For Linux

<img alt="blender-render-background-screenshot.png" src="blender-render-background-screenshot.png">

Aplicativo em Python + GTK facilita a Renderização de arquivos `.blend` em segundo plano (modo background) do Blender.

Com a renderização em background você pode dar continuidade com outros projetos no blender.
Seu aquivo .blend deve estar configurado o tipo de saída o "output" para renderização seja em immagem ou vídeo

O icone do programa não poderia ser diferenre dalhe Suzane

<img alt="blender-icon.png" src="blender-icon.png">


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

Execute o programa para ver se seu ambiente já tem as bibliotecas 
nescessárias.

- Python 3.x
- [PyGObject (GTK+3)](https://pygobject.readthedocs.io/en/latest/)
- Blender instalado no sistema

Instale o PyGObject (no Linux):

```
> sudo apt install python3-gi gir1.2-gtk-3.0
```

## 🚀 Como usar
Baixe e realize a extração do arquivo blender-render-background.tar.gz em
um diretório de sua preferencia para posterior execução.

## Execute o programa:

Entre na pasta blender-render-background e execute o arquivo:

```
python3 bldender-render-background.py
```

## Atalho para Execução

Execução via menu é opcional, crie um atalho do programa no menu do Linux
que deseja colocar

Crie um arquivo: blemder-remder-background.desktop

```
[Desktop Entry]
Version=1.0
Type=Application
Name=Meu Programa Python
Comment=Executar meu script Python
Exec=python3 /caminho/para/seu/script.py
Icon=/caminho/para/um/ícone.png
Path=/caminho/para/o/diretório/do/script
Terminal=false
Categories=Utility;Application;
Exec: Substitua /caminho/para/seu/script.py pelo caminho completo para o seu script Python.
Icon: (Opcional) Substitua pelo caminho para um ícone se desejar um ícone personalizado.
Path: (Opcional) Defina o diretório de trabalho para o script, se necessário.
```

## Transforme o .desktop em execitável
```
chmod +x /caminho/para/blender-render-background.desktop
```
## Copie para a pasta de atalhes

```
mv /***caminho***/para/blender-render-background.desktop ~/.local/share/applications/
```

## Selecione:

Selecione o executável e a versão do Blender em sequidaa selecione seu arquivo .blend desejado 
para renderização e em seguida Clique em "Iniciar Renderização"

##💡 Observações

O caminho do Blender é salvo automaticamente no arquivo blender-render-background.ini , a
renderização é feita em background usando em um subprocess. 

Na tela de execução é informado o PID do Subprocesso que pode ser acompanhado com programa
TOP padão do linux no prompt de comando.

## Doação para o Projeto

Se esse app te ajudou, considere apoiar com uma doação:
Sergop ReOli (Reis de Oliveira)
Paypal: sergioreoli@hotmail.com

## Estrutura sugerida do repositório

```
blender-render-background/
├── icons/-
│   └── blender-icon.png
├── docs/
│   └── blender-render-background.screenshot.png (opcional)
├── blender-render-background-v2.py
├── blender-render-background.ini
├── README.md
├── LICENSE
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

