#!/usr/bin/python3
"""
Deploys archive to remote server.
"""

from fabric.api import put, run, env
import os

env.hosts = ['35.174.204.16', '100.26.169.103']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    This functions transfers compressed web_static content to
    the specified hosts server, decompresses them and deploy then
    for the web_server to serve

    Argument: string -> path to archived contents
    return: True if all operations were successful
            False if any failed or archive passed doesn't exist.
    """

    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the remote server
        put(local_path=archive_path, remote_path='/tmp/')

        # Decompresses Archive
        new_release = archive_path.split('/')[-1].replace('.tgz', '')
        run('mkdir -p /data/web_static/releases/{}'.format(new_release))
        run('tar -xf /tmp/{} -C /data/web_static/releases/{}'
            .format(archive_path.split('/')[-1], new_release))
        run('rm /tmp/{}'.format(archive_path.split('/')[-1]))

        # Updates Symbolic link
        run('rm /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(new_release))
        run('echo "Holberton School" > /data/web_static/current/my_index.html')
        run('mv /data/web_static/releases/{}/web_static/* '
            .format(new_release) + '/data/web_static/current')
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(new_release))
        print("New version deployed")
        return True
    except Exception as e:
        print(f"Deployment Failed")
        return False
# #!/usr/bin/python3

# from fabric.api import run, put, env
# from os import path
# # from datetime import datetime

# # Set the remote hosts, user, and key file for Fabric
# env.hosts = ['35.174.204.16', '100.26.169.103']
# env.user = 'ubuntu'
# env.key_filename = ['/home/john/.ssh/id_rsa']


# def do_deploy(archive_path):
#     """
#     Distributes an archive to web servers and deploys it.

#     :param archive_path: Path to the local archive to be deployed
#     :return: True if deployment is successful, False otherwise
#     """

#     try:
#         # Check if the local archive exists
#         if not path.exists(archive_path):
#             return False

#         # Upload the archive to /tmp/ directory on web servers
#         put(archive_path, '/tmp/')

#         # Extract timestamp from the archive path
#         timestamp = archive_path[-18:-4]

#         # Create target directory for deployment
#         run('sudo mkdir -p /data/web_static/releases/web_static_{}/'.format(
#             timestamp))

#         # uncompress archive and delete .tgz
#         run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
# /data/web_static/releases/web_static_{}/'
#             .format(timestamp, timestamp))

#         # Remove the uploaded archive
#         run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

#         # Move contents into the host web_static directory
#         run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
# /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

#         # remove extraneous web_static dir
#         run('sudo rm -rf /data/web_static/releases/\
# web_static_{}/web_static'
#             .format(timestamp))

#         # delete pre-existing sym link
#         run('sudo rm -rf /data/web_static/current')

#         # re-establish symbolic link
#         run('sudo ln -s /data/web_static/releases/\
# web_static_{}/ /data/web_static/current'.format(timestamp))

#         print("New version deployed!")

#     except Exception as e:
#         return False

#     # return True on success
#     return True