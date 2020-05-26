set nocompatible
filetype plugin indent on

"COLORS
syntax enable       " Enable syntax processing
set t_Co=256

" VUNDLE PLUGIN MANAGER
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" Plugin Begin - All plugins must be included between Begin and End
Plugin 'VundleVim/Vundle.vim'
Plugin 'vim-pandoc/vim-pandoc'
Plugin 'tpope/vim-fugitive'
Plugin 'airblade/vim-gitgutter'
Plugin 'vimwiki/vimwiki'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'mattn/calendar-vim'
Plugin 'xuhdev/vim-latex-live-preview'
Plugin 'hdima/python-syntax'
" Plugin End - All plugins must be included between Begin and End
call vundle#end()

" SPACES TABS AND SPECIAL CHARACTERS
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

" Python & LaTex Indentation
au BufNewFile,BufRead *.py,*.tex
    \ set tabstop=4
    \ set softtabstop=4
    \ set shiftwidth=4
    \ set textwidth=79
    \ set expandtab
    \ set autoindent
    \ set fileformat=unix

" Web Indentation
au BufNewFile,BufRead *.js,*.html,*.css
    \ set tabstop=2
    \ set softtabstop=2
    \ set shiftwidth=2

" UI CONFIG
set ttimeoutlen=10
set visualbell
set noerrorbells
set number          " Show line numbers
set ruler
set hidden
set encoding=utf-8
set showcmd         " Show command in bottom bar
set laststatus=2    " Alwasy display the statusline
set cmdheight=2     " Set command window height to 2 lines
set nocursorline    " Highlight current line
set wildmode=list:longest,full
set wildmenu
set lazyredraw
set showmatch       " Highlight matching parenthesis
set showmode
set confirm
set undolevels=1000
set history=1000
set shell=bash
set updatetime=250
set nospell

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
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-L>

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

" ABBREVIATIONS
iabbrev john@ jtknowles007@gmail.com
iabbrev rn@ johntknowlesrn@gmail.com

" LATEX
autocmd FileType tex nnoremap <F5> :!xelatex<Space><C-R>%<CR>
autocmd FileType tex inoremap <F5><Esc> :!xelatex<Space><C-R>%<Enter>a
autocmd FileType tex nnoremap <F4> :!pdflatex<Space><C-R>%<CR><CR>
autocmd FileType tex inoremap <F5><Esc> :!pdflatex<Space><C-R>%<Enter>a
autocmd FileType tex map <F3> :w !detex\|wc -w<CR>
autocmd FileType tex inoremap <F3><Esc> :w !detex\|wc -w<CR>
autocmd FileType tex nnoremap <leader>p :!atril <C-R>%<backspace><backspace><backspace>pdf &<CR><CR>

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

" VIMWIKI INTEGRATION
let g:vimwiki_list = [
    \{'path': '~/VimWiki/linux.wiki', 'path_html': '~/Projects/www/html/wiki/linux'},
    \{'path': '~/VimWiki/personal.wiki', 'path_html': '~/Projects/www/html/wiki/personal'},
    \{'path': '~/VimWiki/wgu.wiki', 'path_html': '~/Projects/www/html/wiki'}]

au BufRead, BufNewFile *.wiki set filetype=vimwiki
:autocmd FileType vimwiki map d:VimwikiMakeDiaryNote
function! ToggleCalendar()
    execute ":Calendar"
    if exists("g:calendar_open")
        if g:calendar_open ==1
            execute "q"
            unlet g:calendar_open
        else
            g:calendar_open = 1
        end
    else
        let g:calendar_open = 1
    end
endfunction
:autocmd FileType vimwiki map c :call ToggleCalendar()

" ULTISNIPS INTEGRATION
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"
let g:UltiSnipsEditSplit="vertical"

" LIVEPREVIEW INTEGRATION
let g:livepreview_previewer='atril'

" AIRLINE INTEGRATION
let g:airline_theme='zenburn'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'
