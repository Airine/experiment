# Experiment for myFi

Our system requires minimum modification on the existing infrastructure. MyFi is expected to be compatible with any normal WiFi router. A copy of our programs is stored and executed in a Raspberry Pi, which is connected to the router and handles almost everything. Meanwhile, the router keeps working as normal, except that the Dynamic Host Configuration Protocol (DHCP) configuration is taken over by our programs. We test our implementation with a normal WiFi router and a Raspberry Pi, same as the deployment of our system in real world. Users are emulated with Docker. We evaluate the performance by first testing the validity and effectiveness of the user-level service differentiation. Afterwards, we measure the improvement of QoS received by users after our system is deployed. We focus on the quality of video streaming services, which is the most popular representative of content delivery services. Popular providers such as Netflix and YouTube have already accounted for over half of peak-time traffic. Great quality of connection and effective service differentiation will be beneficial for video streaming.

## A[.](./1-validity) Validity and Effectiveness

We evaluate the effectiveness of our smart contract and WiFi controller with iPerf, which actively measures the maximum achievable bandwidth on IP networks. Emulated users submit demand for bandwidth and data burst. We then check if the received quality of connection matches the results directly derived from our allocation and pricing mechanisms.

## B[.](./2-scalability) Performance and Scalability

We have implemented different versions of systems that both support permissionless and permissioned blockchains. Our system works more efficiently on a permissioned one, which generally takes shorter to confirm a transaction due to the additional authorization.

## C[.](./3-qos) Improvement of Service Quality

Dynamic Adaptive Streaming over HTTP (DASH) provides adaptive streaming of videos. Segmented media contents are encoded in various bit rates, and are adjusted subject to the network condition. Therefore, the real-time video quality directly reflects the available quality of connection.
