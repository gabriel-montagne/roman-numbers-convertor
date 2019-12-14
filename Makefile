test:
	@ echo 'start tests ..'
	@ pytest ./tests/test.py
	@ echo 'tests ended ..'

deploy:
	@ echo 'Start cloud deploy ...'
	@ gcloud beta functions deploy handler --runtime python37 --trigger-http --project=$$PROJECT_NAME
	@ echo 'Deploy ended...'

local:
	@ echo 'Start local server ...'
	@ python main.py
