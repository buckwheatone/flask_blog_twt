import os
import tempfile 
import pytest 

from website import create_app


 

@pytest.fixture 
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({'TESTING': True, 'DATABASE': db_path})

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client 
    
    os.close(db_fd)
    os.unlink(db_path) 


# Things to potentially test. 
# 200 response from each page
# login successfully with correct credentials -- response 200 from home
# login unsuccessfully with correct email, wrong password -- response 200 from login
# lonin unsuccessfully with incorrect email -- response 200 from login
