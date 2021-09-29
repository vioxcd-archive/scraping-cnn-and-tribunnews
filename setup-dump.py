import os

ROOT_FOLDER = 'dump'
CNN_FOLDER = 'dump/cnn'
TRIBUN_FOLDER = 'dump/tribun'
CNN_ARTICLES_FOLDER = 'dump/cnn/articles'
CNN_LINKS_FOLDER = 'dump/cnn/link'

def create_folder_if_not_exist(path, name):
	if not os.path.exists(path):
		print(f'{name} folder not found: creating..')
		os.mkdir(path)

def setup_dump_folder_tree():
	create_folder_if_not_exist(ROOT_FOLDER, 'Dump')
	create_folder_if_not_exist(CNN_FOLDER, 'CNN')
	create_folder_if_not_exist(CNN_ARTICLES_FOLDER, 'CNN articles')
	create_folder_if_not_exist(CNN_LINKS_FOLDER, 'CNN links')
	create_folder_if_not_exist(TRIBUN_FOLDER, 'Tribun')

if __name__ == '__main__':
	print('Setting up dump folder tree...')
	setup_dump_folder_tree()
	print('Setup completed. check your folder tree')
