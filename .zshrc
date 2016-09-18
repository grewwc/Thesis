export ZSH=$HOME/.oh-my-zsh
ZSH_THEME="kphoen"
export PATH=$HOME/bin:/usr/local/bin:$PATH

source $ZSH/oh-my-zsh.sh
# #MAKE DER ZSH SING FOR ITS SUPPER
 
## Lets set some options
 
## Set some ZSH auto complete options
 
## History stuffs
HISTFILE=~/.zsh-histfile
HISTSIZE=5000
SAVEHIST=5000
 
#ALIASES

##ls, the common ones I use a lot shortened for rapid fire usage
alias python='python3'
#alias jjupyter='jupyter qtconsole --ConsoleWidget.font_size=19'
alias jupyterq='jupyter qtconsole'
alias jupytern='jupyter notebook'
alias ll='ls -l'
alias xe='xelatex'
alias copy='cp account Google\ Drive'
alias grep='grep --color=auto'
export PYTHONSTARTUP=$HOME/.pystartup.py
export LC_ALL=en_US.UTF-8  
export LANG=en_US.UTF-8
#alias vim='mvim'


