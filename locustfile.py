from locust import task, FastHttpUser


class LocustTestUser(FastHttpUser):
    @task(4)
    def index(self):
        self.client.get("/index")

    @task
    def moreload(self):
        self.client.get("/moreload")
