def deploy():
	"""Run deployment tasks."""
	from app import create_app,db

	app = create_app()
	app.app_context().push()

	# create database and tables
	db.create_all()
	
deploy()