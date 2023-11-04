### repo for semi automaticaly setting addlist for adguard

## repo contains manifest and instructions

# to build:

    docker build -t adguard-adlist-builder

# to run: 

    docker run -e HOST=<hostname> -e USER=<basic_auth_username> -e PASS=<basic_auth_password> -v <local_path_to_file>:/raw_url

# example 

    docker run -e HOST=http://10.0.0.5 -e USER=my_super_secret_username -e PASS=my_super_secret_password -v /home/myUser/files/script_file:/raw_url

# notes:
    for the input file the important format is that each url is in a new line, and it starst with http(s)


credits for the crtipts mostly go to reddit users: carzian and esei1356