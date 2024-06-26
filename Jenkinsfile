pipeline {
    agent any // Any available Jenkins agent can execute this pipeline

    stages {
        stage('Checkout Code') {
            steps {
                // Assuming your code is in a Git repository
                git 'https://your-git-repo-url.git' 
            }
        }

        stage('Run Selenium Test') {
            steps {
                // Install necessary dependencies
                sh 'pip install selenium'  // Example: Install Selenium using pip

                // Set up environment variables
                sh 'export PATH=$PATH:/path/to/chromedriver' // Update with your chromedriver path

                // Execute the Python test script
                sh 'python your_selenium_test_script.py'  // Replace with your actual script name
            }
        }
    }
}
