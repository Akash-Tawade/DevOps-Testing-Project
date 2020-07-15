pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '5365601b-2fc9-4d1f-a882-a28309e931d3', url: 'https://github.com/Akash-Tawade/DevOps-Testing-Project.git']]])
            }
        }
        stage('code analysis') {
            steps {
                echo 'This code had beeen analysis'
            }
        }
        stage('code deploment') {
            steps {
                echo 'This code has been deployed'
            }
        }
    }
}
