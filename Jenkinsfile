pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Baimurat'
        STUDENT_SURNAME = 'Akbiyev'
        STUDENT_GROUP = 'IT2-2306'
        STUDENT_ID = '38150'

        IMAGE_NAME = 'akbiyev-baimurat-devops'
        CONTAINER_NAME = 'akbiyev-baimurat-jenkins'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking project structure...'

                sh '''
                    test -f Dockerfile
                    test -f app/app.py
                    test -f app/test_app.py
                    test -f config/app.conf
                    test -f Akbiyev_Baimurat_info.txt
                '''

                echo 'Project structure is valid.'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python unit tests...'

                sh '''
                    docker build \
                      --target test \
                      -t "$IMAGE_NAME:test" \
                      .
                '''

                echo 'All tests passed.'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building production Docker image...'

                sh '''
                    docker build \
                      --target runtime \
                      -t "$IMAGE_NAME:latest" \
                      .
                '''
            }
        }

        stage('Docker Run') {
            steps {
                echo 'Starting application container...'

                sh '''
                    docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

                    docker run -d \
                      --name "$CONTAINER_NAME" \
                      -e STUDENT_NAME="$STUDENT_NAME" \
                      -e STUDENT_SURNAME="$STUDENT_SURNAME" \
                      -e STUDENT_GROUP="$STUDENT_GROUP" \
                      -e STUDENT_ID="$STUDENT_ID" \
                      "$IMAGE_NAME:latest"

                    docker exec "$CONTAINER_NAME" \
                      python -c "import time,urllib.request; url='http://127.0.0.1:8000'; time.sleep(2); print(urllib.request.urlopen(url,timeout=10).read().decode())"

                    docker logs "$CONTAINER_NAME"
                '''
            }
        }
    }

    post {
        success {
            echo '================================'
            echo 'PIPELINE COMPLETED SUCCESSFULLY'
            echo '================================'

            echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
            echo "Group: ${env.STUDENT_GROUP}"
            echo "Student ID: ${env.STUDENT_ID}"
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
