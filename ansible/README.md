# How to run the playbooks
1. `cd` into this directory
2. Run 

    `ansible-playbook -i inventory.ini --ask-pass setup_transmitter_playbook.yml` or
    
    `ansible-playbook -i inventory.ini --ask-pass setup_receiver_playbook.yml` to setup the Raspberry Pi as the receiver or the transmitter.
