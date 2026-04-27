**Canary Deployment** is the process where % of the traffic is sent to the newer version of the code unlike the rolling update where the complete traffic is sent to new version of the app.

Two deployments - v1 and v2

In this case v1 is the latest compared to v2.

Updating the deployment labels to v1 and v2 and the respective images code changes return version 1 and version 2

Pods:

<img width="962" height="167" alt="image" src="https://github.com/user-attachments/assets/ba5f0396-7474-417a-8bdc-c2b1d8cc03b6" />


```
kubectl -n devops-cluster run debug --rm -it --image=curlimages/curl -- sh
~ $  for i in $(seq 1 20); do curl python-app-service; echo; done

App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password
 <br>
Version: v1
```
Here, we can see the requests to V1 and V2 pods were forwareded almost equally.


Now, I tried to scale down the v1 replicas to simulate the canary deployment, now the maximum requests will be served to the v2 version


Below is the output.

Pods:
```
k scale deploy python-app-deployment-v1 --replicas=1
deployment.apps/python-app-deployment-v1 scaled
unix@Hp:~$ k get po
NAME                                        READY   STATUS        RESTARTS   AGE
debug                                       1/1     Running       0          3m33s
python-app-deployment-v1-dfbf9bbf5-58sxr    1/1     Terminating   0          130m
python-app-deployment-v1-dfbf9bbf5-n7vwt    1/1     Terminating   0          130m
python-app-deployment-v1-dfbf9bbf5-v9rx8    1/1     Running       0          130m
python-app-deployment-v2-7b555556b7-5c9m8   1/1     Running       0          130m
python-app-deployment-v2-7b555556b7-dd5sw   1/1     Running       0          130m
python-app-deployment-v2-7b555556b7-vwjjd   1/1     Running       0          130m
```


Output: 
```
~ $  for i in $(seq 1 20); do curl python-app-service; echo; done

App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password
 <br>
Version: v1


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password

Version: v2<br>


App Color: white<br>
DB Password: password
 <br>
Version: v1
```

