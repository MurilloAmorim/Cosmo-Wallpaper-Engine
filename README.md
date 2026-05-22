# Cosmo Wallpaper Engine

O **Cosmo Wallpaper Engine** é uma aplicação de automação desktop desenvolvida em Python que consome a API oficial da NASA para buscar a "Foto Astronômica do Dia" (APOD) e integrá-la dinamicamente como plano de fundo do sistema operacional Windows.

Este projeto foi construído com foco em **arquitetura limpa, segurança da informação, integração com o sistema operacional e experiência do usuário (UX)**.

---

## Funcionalidades

- **Consumo Automatizado de API:** Realiza requisições assíncronas para a API da NASA (`APOD`) assim que a aplicação é iniciada.
- **Fluxo com Pré-visualização Inteligente (UX):** Diferente de scripts de automação comuns, este aplicativo renderiza uma prévia da imagem, título e descrição científica em uma interface gráfica, permitindo que o usuário decida se deseja aplicar o wallpaper.
- **Validação e Tratamento de Mídias:** O sistema identifica se o conteúdo diário da NASA é uma imagem ou um vídeo, tratando a exceção de forma amigável para o usuário caso não seja um formato aplicável.
- **Automação a Nível de Kernel (Win32 API):** Utiliza bibliotecas de baixo nível para interagir diretamente com a API do Windows (`user32.dll`), alterando as configurações do sistema nativamente.
- **Tratamento de Erros:** Sistema preparado para gerenciar códigos de status HTTP (como erro 403 de credenciais inválidas) e falhas de conexão de rede sem travar o software.

---

## Tecnologias Utilizadas

- **Python 3**
- **Tkinter:** Arquitetura e renderização da interface gráfica (GUI).
- **Pillow (PIL):** Processamento de imagens em alta definição, redimensionamento dinâmico e conversão forçada de canais de cor (RGB) para compatibilidade de tela.
- **Requests:** Gerenciamento de requisições HTTP, captura de payloads JSON e download de arquivos binários.
- **Python-Dotenv:** Proteção e isolamento de dados sensíveis utilizando variáveis de ambiente.
- **Ctypes:** Ponte de integração entre o código Python e as bibliotecas nativas em C do Windows.

---

## Segurança e Boas Práticas Empregadas

- **Zero Hardcoded Credentials:** Nenhuma chave de API ou credencial sensível fica exposta no código fonte; todas são gerenciadas de forma segura via arquivos `.env`.
- **Estratégia de Gitignore:** Repositório configurado estritamente para não rastrear ambientes virtuais (`.venv/`), caches e chaves privadas de configuração local.
- **Gerenciamento Seguro de Memória:** O código foi refatorado sob o escopo de funções isoladas (`main()`), aplicando técnicas de "âncora de referência" para evitar que o Garbage Collector do Python delete componentes visuais em tempo de execução.

---

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU_USUARIO_AQUI/CosmoWallpaperEngine.git](https://github.com/SEU_USUARIO_AQUI/CosmoWallpaperEngine.git)
cd CosmoWallpaperEngine
