from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    @task
    def get_data(self):
        self.client.get("/")

    @task
    def post_data(self):
        self.client.post("/data", json={"key": "value"})


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(0.1, 0.3)
    host = "http://0.0.0.0:8000"
