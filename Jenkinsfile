pipeline {
    agent {
        docker {
            image 'registry.mahnke.tech/dbox/python:2025-03.01'
            args '-v pcm_cache:/var/cache/pdm -e PDM_CACHE_DIR=/var/cache/pdm'
            reuseNode true
        }
    }

    stages {
        stage('Clean workspace') {
            steps {
                sh 'git clean -dfx'
            }
        }

        stage('Install') {
            steps {
                sh 'pdm install'
            }
        }

        stage('Check') {
            steps {
                sh 'pdm run nox'
            }
        }
    }

    triggers {
        cron('H H * * *')
        pollSCM('*/5 * * * *')
    }
}
