import os
import shutil


class fs:

    @staticmethod
    def ls(path='.', toEcho=True, fullPath=False):
        """
        List files in a directory
        """
        if (fullPath is True):
            files = [os.path.join(path, file) for file in os.listdir(path)]
        else:
            files = os.listdir(path)
            
        if (toEcho is True):
            for file in files:
                print(file)
        return files

    @staticmethod
    def mkdir(path, mode=0o777, exist_ok=True):
        """
        Create a directory recursively similar to `mkdir -p` in Linux
        """
        os.makedirs(path, mode, exist_ok)

    @staticmethod
    def rm(path, recursive=False):
        """
        Remove files or directories (directories require recursive=True)
        """
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path) and recursive:
            shutil.rmtree(path)
        elif os.path.isdir(path) and not recursive:
            os.rmdir(path)

    @staticmethod
    def cp(src, dst):
        """
        Copy files or directories recursively
        """
        if os.path.isfile(src):
            shutil.copy2(src, dst)
        else:
            shutil.copytree(src, dst)

    @staticmethod
    def mv(src, dst):
        """
        Move files or directories recursively
        """
        shutil.move(src, dst)

    @staticmethod
    def pwd():
        """
        Print the current working directory
        """
        return os.getcwd()

    @staticmethod
    def cd(path):
        """
        Change the current working directory
        """
        os.chdir(path)