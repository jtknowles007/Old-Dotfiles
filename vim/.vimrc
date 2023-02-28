set nocompatible
set noswapfile
filetype on
filetype plugin on
filetype indent on
set viminfofile=NONE

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"COLORS
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" General
syntax on       " Enable syntax processing

" Python
let python_highlight_all = 1


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" PLUGINS
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" Plugin Begin - All plugins must be included between Begin and End
Plugin 'airblade/vim-gitgutter'
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'morhetz/gruvbox'
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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" GLOBAL VARIABLES
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Code Completion
let g:kite_supported_languages = ['python', 'javascript']

" NERDTree Menu
let g:NERDTreeQuitOnOpen=1
let g:WebDevIconsUnicodeDecorateFolderNodes = 1
let g:WebDevIconsUnicodeDecorateFolderNodeDefaultSymbol = '#'
let g:WebDevIconsUnicodeDecorateFileNodesExtensionSymbols = {}
let g:WebDevIconsUnicodeDecorateFileNodesExtensionSymbols['nerdtree'] = '#'

autocmd vimenter * NERDTree
autocmd vimenter * wincmd p
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
set signcolumn=yes
set ruler
set hidden
set encoding=utf-8
set showcmd         " Show command in bottom bar
set laststatus=2    " Always display the status line
set cmdheight=2     " Set command window height to 2 lines
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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" KEY MAPPING
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Custom Leader
let mapleader=","

" New Splits
nnoremap <leader>ev :vsplit $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>

" Navigate Splits with Arrow Keys in Normal Mode
map <up> <C-w><up>
map <down> <C-w><down>
map <left> <C-w><left>
map <right> <C-w><right>

" Navigate by Display Line not Physical Line
nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk

" Add/Remove highlighting of characters past column 80
map <leader>ll :match Error /\%>80c/<CR>
map <leader>lc :match none<CR>

" Remove search highlighting
map <silent> <leader><CR> :noh<CR>

" Folding
nnoremap <space> za

" Custom Function Mapping
nnoremap <leader>l :call ToggleNumber()<CR>
nnoremap <leader>w :set list!<CR>
nnoremap <leader>s :set spell!<CR>

" Comment Blocks
map <F2> :s/^\(.*\)$/#\1/g<CR>      " Comment selected block with #
map <F3> :s/^#//g<CR>               " Uncomment block with #

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" SPELLCHECK
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Highlighting
hi clear SpellBad
hi SpellBad cterm=underline,bold ctermfg=red

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" SAVE LOCATIONS
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set backupdir=.backup/,~/.backup/,/tmp//
set undodir=.undo/,~/.undo/,/tmp//
set directory=.swp/,~/.swp/,/tmp//

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" CUSTOM FUNCTIONS
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
function! ToggleNumber()
    if(&relativenumber ==1)
        set norelativenumber
        set number
    else
        set relativenumber
    endif
endfunction

set statusline=
set statusline+=%#DiffAdd#%{(mode()=='n')?'\ \ NORMAL\ ':''}
set statusline+=%#DiffChange#%{(mode()=='i')?'\ \ INSERT\ ':''}
set statusline+=%#DiffDelete#%{(mode()=='r')?'\ \ RPLACE\ ':''}
set statusline+=%#Cursor#%{(mode()=='v')?'\ \ VISUAL\ ':''}
set statusline+=\ %n\           " buffer number
set statusline+=%#Visual#       " colour
set statusline+=%{&paste?'\ PASTE\ ':''}
set statusline+=%{&spell?'\ SPELL\ ':''}
set statusline+=%#CursorIM#     " colour
set statusline+=%R                        " readonly flag
set statusline+=%M                        " modified [+] flag
set statusline+=%#Cursor#               " colour
set statusline+=%#LineNrAbove#     " colour
set statusline+=\ %t\                   " short file name
set statusline+=%=                          " right align
set statusline+=%#SignColumn#   " colour
set statusline+=\ %Y\                   " file type
set statusline+=%#SignColumn#     " colour
set statusline+=\ %3l:%-2c\         " line + column
set statusline+=%#SignColumn#       " colour
set statusline+=\ %3p%%\                " percentage
