pipeline {
    agent { dockerfile true }

    stages {
        stage('Check') {
            steps {
                sh 'nox'
            }
        }
    }

    triggers {
        cron('H H * * *')
        pollSCM('*/5 * * * *')
    }
}
