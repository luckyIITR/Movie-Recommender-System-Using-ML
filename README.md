Sure! Here’s the complete README.md file code you can copy-paste directly into your project:

⸻



# 🎬 Movie Recommender System

A simple and interactive movie recommender system built with **Streamlit** and **TMDb API**, powered by **Machine Learning**. 

Users can select any movie and receive 5 similar recommendations with posters, genres, ratings, and descriptions.

---

## 🚀 Demo

🧪 Run locally:  
```bash
streamlit run app.py



⸻

📦 Features
	•	✅ ML-based recommendation engine using cosine similarity
	•	🎞️ Real-time poster & movie details from TMDb API
	•	⚡ Fast and clean UI using Streamlit
	•	🔍 Searchable dropdown for movie selection
	•	🌐 Deploy-ready on AWS with Nginx & systemd support

⸻

🧠 How it Works
	1.	A precomputed similarity matrix is generated using movie features.
	2.	When a user selects a movie, the system:
	•	Finds the most similar movies based on cosine similarity
	•	Fetches their details from TMDb
	•	Displays poster, title, genres, rating, and overview

⸻

🛠️ Installation
	1.	Clone the repo:

git clone https://github.com/yourusername/movie-recommender-streamlit.git
cd movie-recommender-streamlit

	2.	Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

	3.	Install dependencies:

pip install -r requirements.txt

	4.	Set up your .env file:

TMDB_API_KEY=your_tmdb_api_key_here

	5.	Run the app:

streamlit run app.py



⸻

📁 Project Structure

movie-recommender-streamlit/
├── artifacts/
│   ├── movie_list.pkl          # Pickled movie DataFrame
│   └── similarity.pkl          # Cosine similarity matrix
├── app.py                      # Main Streamlit app
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── .env                        # API key (not committed)



⸻

📌 Dependencies
	•	streamlit
	•	requests
	•	python-dotenv
	•	pandas
	•	scikit-learn (if preprocessing used before pickle)
	•	pickle (Python built-in)

⸻

🌐 Deployment Guide (AWS + Nginx + systemd)
	1.	SSH into your AWS instance:

ssh ubuntu@your-aws-ip

	2.	Clone or copy your project to the server.
	3.	Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

	4.	Test your app:

streamlit run app.py --server.port 8501 --server.headless true

	5.	Create a systemd service (/etc/systemd/system/streamlit.service):

[Unit]
Description=Streamlit App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/movie-recommender-streamlit
ExecStart=/home/ubuntu/movie-recommender-streamlit/venv/bin/streamlit run app.py --server.port 8501 --server.headless true
Restart=always

[Install]
WantedBy=multi-user.target

	6.	Enable and start the service:

sudo systemctl daemon-reload
sudo systemctl enable streamlit
sudo systemctl start streamlit

	7.	Configure Nginx as a reverse proxy:

location /movies/ {
    proxy_pass http://localhost:8501/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}

	8.	(Optional) Enable SSL:

sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx



⸻

🔐 TMDb API Key

Get a free TMDb API key here:
🔗 https://www.themoviedb.org/settings/api

Save it in a .env file like this:

TMDB_API_KEY=your_api_key_here



⸻

📸 Example Output

You can add a screenshot or demo GIF here once the app is running

![UI Screenshot](assets/example-ui.png)



⸻

📜 License

This project is open-source under the MIT License.

⸻

🙋‍♂️ Author

Developed by Your Name

Feel free to reach out or contribute!

---

Let me know your name or GitHub username if you'd like it personalized at the bottom. I can also generate the `requirements.txt` if needed.