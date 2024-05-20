from celery.result import AsyncResult
from example.ch10_02.celery_app import celery

if __name__ == "__main__":
    async_result = AsyncResult("87d02ecc-e15e-4769-9cd5-b02283c3506f", app=celery)
    result = async_result.result
 
    print(result)
