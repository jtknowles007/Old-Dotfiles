set nocompatible
set noswapfile
filetype plugin indent on

let g:kite_supported_languages = ['python', 'javascript']

"COLORS
syntax on       " Enable syntax processing
" set background=light
let g:solarized_termcolors=256
colorscheme pyte


" VUNDLE PLUGIN MANAGER
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" Plugin Begin - All plugins must be included between Begin and End
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
" Plugin 'airblade/vim-gitgutter'
" Plugin 'hdima/python-syntax'
Plugin 'morhetz/gruvbox'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'ryanoasis/vim-devicons'
Plugin 'scrooloose/nerdcommenter'
Plugin 'sheerun/vim-polyglot'
Plugin 'jiangmiao/auto-pairs'
Plugin 'neoclide/coc.nvim', {'branch': 'release'}
Plugin 'davidhalter/jedi-vim'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'
Plugin 'PhilRunninger/nerdtree-visual-selection'
Plugin 'junegunn/vim-easy-align'
Plugin 'https://github.com/junegunn/vim-github-dashboard.git'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }
Plugin 'tpope/vim-fireplace', { 'for': 'clojure' }
" Plugin End - All plugins must be included between Begin and End
call vundle#end()

let g:bargreybars_auto=0
let g:airline_solorized_bg='light'
let g:airline_powerline_fonts=1
let g:airline#extension#tabline#enable=1
let g:airline#extension#tabline#left_sep=' '
let g:airline#extension#tabline#left_alt_sep='|'
let g:airline#extension#tabline#formatter='unique_tail'
let NERDTreeQuitOnOpen=1

let g:WebDevIconsUnicodeDecorateFolderNodes = 1
let g:WebDevIconsUnicodeDecorateFolderNodeDefaultSymbol = '#'
let g:WebDevIconsUnicodeDecorateFileNodesExtensionSymbols = {}
let g:WebDevIconsUnicodeDecorateFileNodesExtensionSymbols['nerdtree'] = '#'


autocmd vimenter * NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
map <C-n> :NERDTreeToggle<CR>

"SPACES TABS AND SPECIAL CHARACTERS
set tabstop=4       " 4 space tab
set expandtab       " use spaces for tabs
set softtabstop=4   " 4 space tab
set shiftwidth=4
set autoindent
set copyindent
set smartindent
set smarttab
set backspace=indent,eol,start
set nolist
set listchars=tab:▶-,trail:•,extends:»,precedes:«,eol:¬

" UI CONFIG
set ttimeoutlen=10
set visualbell
set noerrorbells
set number          " Show line numbers
set ruler
set hidden
set encoding=utf-8
set showcmd         " Show command in bottom bar
set laststatus=2    " Always display the status line
set cmdheight=2     " Set command window height to 2 lines
set cursorline    " Highlight current line
set wildmode=list:longest,full
set wildmenu
set lazyredraw
set showmatch       " Highlight matching parenthesis
set showmode
set confirm
set undolevels=1000
set history=1000
set shell=zsh
set updatetime=250
set spell
set ttyfast
set buftype=""
set clipboard=unnamedplus
set completeopt=noinsert,menuone,noselect
set mouse=a
set splitbelow splitright
set title
set guifont=hack_nerd_font:h11

" SEARCHING
set ignorecase      " Ignore case when searching
set smartcase       " Except when using capital letters 
set incsearch       " Search as characters are entered
set hlsearch        " Highlight all matches

" FOLDING
set foldmethod=indent   " Fold based on indent level
set foldnestmax=10      " Max 10 depth
set foldenable
set foldlevelstart=10

" DISABLE ARROW KEYS
map <up> <nop>
map <down> <nop>
map <left> <nop>
map <right> <nop>
inoremap <up> <nop>
inoremap <down> <nop>
inoremap <left> <nop>
inoremap <right> <nop>

" EASIER SPLIT NAVIGATION
" Navigate panes with arrow keys
map <up> <C-w><up>
map <down> <C-w><down>
map <left> <C-w><left>
map <right> <C-w><right>

" CUSTOM LEADER
let mapleader=","

" CUSTOM KEY BINDINGS
nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk
map <silent> <leader><CR> :noh<CR>
nnoremap <space> za
nnoremap <leader>l :call ToggleNumber()<CR>
nnoremap <leader>w :set list!<CR>
nnoremap <leader>s :set spell!<CR>
nnoremap <leader>ev :vsplit $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>

" SAVE LOCATIONS OF SWAP, BACKUP, UNDO
set backupdir=.backup/,~/.backup/,/tmp//
set undodir=.undo/,~/.undo/,/tmp//
set directory=.swp/,~/.swp/,/tmp//

" PYTHON
let python_highlight_all = 1

" CUSTOM FUNCTIONS
function! ToggleNumber()
    if(&relativenumber ==1)
        set norelativenumber
        set number
    else
        set relativenumber
    endif
endfunc
