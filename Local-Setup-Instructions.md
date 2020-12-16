# Prerequisites
1. Boot into your PI
2. Install git with `sudo apt-get install git`
3. If desired you can setup an SSH key to use with GitLab to prevent having to enter your GitLab credentials.

# Initial Repo Setup
1. First run the commands `cd ~` and `mkdir sisbot-server`
2. Change into the sisbot-server directory and clone the MSOE sisbot, siscloud, and sisproxy repos from GitLab. 
3. Rename each directories in the sisbot-server to `sisbot, sisproxy, and siscloud`

# Python Setup
1. Install pip by running the command `sudo apt-get install python-pip`
2. Change into the sisbot directory and run the following command `./install-python.sh`
3. Checkout the dev sisbot branch and change into the content directory.
4. Run the command `pip install -e .`

# Node Setup
1. Run the command `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash` to run the nvm setup script
2. Run the command `export NVM_DIR="$HOME/.nvm" [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"` to load nvm.
3. Open a new bash session and verify the installation by running `nvm -v`
4. Run the command `nvm use 8.11.4`

# Finishers
1. Create soft links between each of the git repositories as their "canonical" names:
`ln -s msoe-sisbot sisbot`
`ln -s msoe-sisproxy sisproxy`
`ln -s msoe-siscloud siscloud`

2. Create the directory that sisyphus will log to:
`sudo mkdir /var/log/sisyphus`
