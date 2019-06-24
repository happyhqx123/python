apt update && apt upgrade -y
apt install zip wget curl git openssh zsh python python-dev vim-python -y
termux-setup-storage
echo "deb [trusted=yes] http://termux.iikira.com stable main" >> /data/data/com.termux/files/usr/etc/apt/sources.list
apt update
apt install baidupcs-go

mkdir $HOME/.termux

echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]" >> $HOME/.termux/termux.properties
cd /data/data/com.termux/files/usr/bin
mv BaiduPCS-Go baidu
cd
