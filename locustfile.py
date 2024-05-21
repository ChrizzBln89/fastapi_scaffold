from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    @task
    def get_data(self):
        self.client.get("/data")

    @task
    def post_data(self):
        self.client.post("/data", json={"key": "value"})


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://0.0.0.0:8000"
