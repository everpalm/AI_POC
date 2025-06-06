pipeline {
    agent {
        label 'AMD64_UBUNTU'
    }
    environment {
        MY_PRIVATE_TOKEN = credentials('gitlab-private-token')
        VERSION_FILE = "${WORKSPACE}/version.txt"
        GIT_TOKEN = credentials('github-token')
        TEST_AMD64 = "${WORKSPACE}/tests/test_amd64"
        TEST_BOOT = "${WORKSPACE}/tests/test_boot"
        TEST_COMMANDLINE = "${WORKSPACE}/tests/test_commandline"
        TEST_DEVICE = "${WORKSPACE}/tests/test_device"
        TEST_INTERFACE = "${WORKSPACE}/tests/test_interface"
        TEST_NETWORK = "${WORKSPACE}/tests/test_network"
        TEST_STORAGE = "${WORKSPACE}/tests/test_storage"
        TEST_UNIT = "${WORKSPACE}/tests/test_unit"
        PATH = "/home/pi/.pyenv/shims:/home/pi/.pyenv/bin:${env.PATH}"
    }
    stages {
        stage('Init') {
            steps {
                script {
                    echo 'Initializing development pipeline...'
                    gv = load "${WORKSPACE}/script.groovy"
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    gv.build_app()
                }
            }
        }
        // stage('Unit Testing') {
        //     steps {
        //         script {
                    // gv.test_pep8(env.TEST_AMD64)
                    // gv.test_pep8(env.TEST_BOOT)
                    // gv.test_pep8(env.TEST_COMMANDLINE)
                    // gv.test_pep8(env.TEST_DEVICE)
                    // gv.test_pep8(env.TEST_INTERFACE)
                    // gv.test_pep8(env.TEST_NETWORK)
                    // gv.test_pep8(env.TEST_STORAGE)
                    // gv.test_pep8(env.TEST_UNIT)
                    // gv.test_unit(env.TEST_UNIT, env.MY_PRIVATE_TOKEN)
        //         }
        //     }
        // }
        stage('Sanity Testing') {
            steps {
                script {
                    sh 'cat Pipfile'
                    sh 'echo "==> check if prefix test exsits"; ls -al .'
                    sh '''
                        if ls test_*.py 1> /dev/null 2>&1; then
                        chmod +x test_*.py
                        echo "shed execution to test_*.py "
                        else
                        echo "None test_*.py file, no need to chmod"
                        fi
                    '''
                    // sh 'chmod +x test_*.py'
                    sh 'pipenv lock'
                    sh 'pipenv run pip list'
                    sh 'pipenv run python3 -m pytest -s'
                    // gv.test_sanity(env.TEST_AMD64)
                    // gv.test_sanity(env.TEST_BOOT)
                    // gv.test_sanity(env.TEST_DEVICE)
                    // gv.test_sanity(env.TEST_INTERFACE)
                    // gv.test_sanity(env.TEST_NETWORK)
                    // gv.test_sanity(env.TEST_STORAGE)
                    // gv.test_regression(env.TEST_COMMANDLINE)
                }
            }
        }
    }
    post {
        always {
            script {
                archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
            }
        }
        success {
            emailext(
                to: 'everpalm@yahoo.com.tw',
                subject: "Build Success: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: """<p>All tests passed successfully!</p>
                         <p>Please check the attached test coverage report.</p>""",
                mimeType: 'text/html',
                attachmentsPattern: 'htmlcov/index.html'
            )
            // script {
            //     try {
            //         sh """
            //         git fetch origin
            //         git checkout staging
            //         git merge origin/staging
            //         git merge origin/development
            //         git push https://everpalm:$GIT_TOKEN@https://github.com/everpalm/AI_POC.git staging
            //         """
            //         build job: 'AutoRAID_Staging', wait: false
            //     } catch (e) {
            //         echo "An error occurred: ${e.getMessage()}"
            //         currentBuild.result = 'FAILURE'
            //     }
            // }
        }
        failure {
            emailext(
                to: 'everpalm@yahoo.com.tw',
                subject: "Build Failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: 'The build has failed. Please check the Jenkins console output for details.',
                mimeType: 'text/html',
                attachmentsPattern: 'htmlcov/index.html'
            )
        }
    }
}
