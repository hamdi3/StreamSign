# StreamSign
[![Powered by Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-ff69b4)](https://www.streamlit.io/)
[![Built with PyTorch](https://img.shields.io/badge/Built%20with-PyTorch-orange)](https://pytorch.org/)
[![Uses ONNX Runtime](https://img.shields.io/badge/Uses-ONNX%20Runtime-blue)](https://onnxruntime.ai/)
[![Uses Matplotlib](https://img.shields.io/badge/Uses-Matplotlib-orange)](https://matplotlib.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://your-docker-hub-repo-url)
[![Deployment](https://img.shields.io/badge/Deployment-Streamlit-blueviolet)](https://streamsign.streamlit.app/)
[![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](https://your-url)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

StreamSign is a web application built using the Streamlit framework for the classification of sign language alphabet. This project serves as my first interaction with Streamlit, where I explore the capabilities of the framework and demonstrate image classification of sign language letters.

## Purpose
The main purpose of this project is to showcase my proficiency in utilizing the Streamlit framework to develop interactive web applications for image classification tasks. By focusing specifically on the classification of sign language alphabet, the project aims to highlight my understanding of computer vision techniques and deep learning models.

## Features
- Web-based user interface for uploading and classifying images of sign language letters.
- Integration with a pre-trained deep learning model for accurate classification.
- Real-time predictions with user-friendly visualization.

## Getting Started
To get started with StreamSign, follow these steps:
1. Clone the repository: `git clone https://github.com/your-username/StreamSign.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`
4. Open your web browser and navigate to `http://localhost:8501` to access the StreamSign interface.

## Docker Installation
To run StreamSign using Docker, follow these steps:
1. Make sure Docker is installed on your system. If not, you can download and install Docker from [here](https://docs.docker.com/get-docker/).
2. Build the Docker image using the provided Dockerfile. Open a terminal or command prompt and navigate to the project directory containing the Dockerfile.
3. Build the image using the following command: `docker build -t streamsign .` 
4. Run the Docker container using the built image: `docker run -p 8501:8501 streamsign` 
5. Open your web browser and navigate to `http://localhost:8501` to access the StreamSign interface.

## Deployment
The StreamSign application is deployed and accessible through the following link:
[https://streamsign.streamlit.app/](https://streamsign.streamlit.app/)

You can visit the above link to access the live version of the application and try it out with your own sign language images.


## Contributing
Contributions to StreamSign are welcome! If you would like to contribute, please follow these guidelines:
- Fork the repository and create your branch: `git checkout -b feature/your-feature`
- Commit your changes: `git commit -am 'Add a feature'`
- Push to the branch: `git push origin feature/your-feature`
- Open a pull request

## License
This project is licensed under the [MIT License](LICENSE).

---
Please note that this project is intended as a showcase of my skills and understanding of the Streamlit framework for web application development. It is not intended for production use. However, feedback and contributions are greatly appreciated.
