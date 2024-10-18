pipeline {
    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'jenkinsPodDefinition.yaml'
        }
    }
    environment {
        DOCKERHUB_REPO = 'robopd2/robopd2-api'
    }
    stages {
        stage ('Clone Repository') {
            steps {
                container('jnlp')  {
                    git url: 'https://github.com/robopd2/robopd2-api.git',
                        branch: 'main',
                        credentialsId: 'robopd2-github-pat'
                }
            }
        }
        stage ('Docker - Build') {
            steps {
                container(name: 'docker') {
                    script {
                        if (env.BRANCH_NAME == 'main') {
                            sh "docker build -t $DOCKERHUB_REPO:latest ."
                            sh "docker build -t $DOCKERHUB_REPO:$BUILD_NUMBER ."
                        } else {
                            sh "docker build -t $DOCKERHUB_REPO:$BUILD_NUMBER ."
                        }
                    }
                }
            }
        }
        stage ('Docker - Push') {
            when {
                branch 'main'
            }
            steps {
                container(name: 'docker') {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                        sh "docker push $DOCKERHUB_REPO:$BUILD_NUMBER"
                        sh "docker push $DOCKERHUB_REPO:latest"
                    }
                }
            }
        }
    }
}