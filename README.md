Serverless AI App with AWS Bedrock
=============================================

This project showcases how to build a fully serverless, AI-powered web application using **AWS Bedrock** and the **Claude foundation model**.  It delivers a lightweight, cost-efficient solution with a clean web interface for interacting with AI-generated responses---ideal for experimentation, demos, and real-world applications.

<img width="1366" height="658" alt="image" src="https://github.com/user-attachments/assets/15a72079-63a0-4886-a600-391d530c812b" />

* * * * *

Features
----------

-   **Serverless Architecture**\
    Built using AWS Lambda and API Gateway for automatic scalability and zero infrastructure management.
-   **Claude Model via AWS Bedrock**\
    Leverages the Claude foundation model through secure Bedrock APIs for intelligent, human-like text generation. You can choose any foundation model available on AWS Bedrock.
-   **Frontend Hosted with GitHub Pages**\
    No additional hosting needed---deploy the UI in seconds using GitHub Pages.
-   **Cost-Efficient**\
    Pay-as-you-go with no need for EC2 or managed servers; great for prototyping or lean deployments.
-   **Simple & Extendable**\
    Clean separation of frontend and backend code makes it easy to customize or extend.

* * * * *

Technologies Used
---------------------

| Component | Purpose |
| --- | --- |
| **AWS Bedrock** | Access foundation models like Claude |
| **AWS Lambda** | Serverless backend to handle model calls |
| **API Gateway** | REST API endpoint routing to Lambda |
| **GitHub Pages** | Hosts the frontend `index.html` file |
| **Python (Boto3)** | Backend logic and Bedrock interaction |

* * * * *

Architecture Flow
---------------------

1.  **GitHub Pages (Frontend)** -- User inputs text via the browser UI.
2.  **API Gateway** -- Forwards requests from the frontend to the backend.
3.  **AWS Lambda** -- Executes serverless logic and invokes Bedrock.
4.  **AWS Bedrock (Claude)** -- Generates a response from the Claude model.
   
* * * * *

Getting Started
------------------

### Prerequisites

-   An active AWS account with Bedrock access.
-   AWS CLI configured with appropriate IAM permissions.
-   A GitHub account with GitHub Pages enabled.
-   Basic familiarity with AWS Lambda and API Gateway.

* * * * *

### 1\. Deploy the Frontend (GitHub Pages)

1.  Fork or clone this repository.
2.  Ensure `index.html` is in the root directory.
3.  In your GitHub repository:
    -   Go to **Settings → Pages**
    -   Under **Source**, select the `main` branch and `/ (root)` folder
    -   Click **Save**
4.  Your app will be live at:\
    `https://your-username.github.io/aws-bedrock-app`

* * * * *

### 2\. Deploy the Backend (AWS Lambda)

1.  Create a new Lambda function via the AWS Console.
    -   Runtime: **Python 3.9 or higher**
    -   Handler: Paste the contents of `lambda_function.py`
2.  **Attach IAM Role** with permission:
    `{
      "Effect": "Allow",
      "Action": "bedrock:InvokeModel",
      "Resource": "*"
    }`

3.  **API Gateway Setup**:
    -   Create a new **HTTP API**
    -   Set integration target to the Lambda function
    -   Enable CORS if needed
    -   Deploy and note the **invoke URL**

* * * * *

### 3\. Connect Frontend to API

1.  Open `index.html` in a code editor.
2.  Locate the JavaScript `fetch()` call.
3.  Replace the placeholder endpoint with your API Gateway invoke URL:
    `fetch("https://your-api-id.execute-api.region.amazonaws.com/prod")`
4.  Commit and push the changes to GitHub.\
    GitHub Pages will update automatically.

* * * * *

Usage
--------

1.  Visit your GitHub Pages site.
2.  Enter a prompt or question in the input box.
3.  Click **Submit**.
4.  The request is sent to your AWS Lambda function.
5.  Lambda invokes Claude via Bedrock and returns the response.
6.  The result is displayed on the web page.
