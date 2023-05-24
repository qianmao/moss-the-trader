# Project Roadmap

## Data source

* (P1) Crate a general interface to query from different api directly.
* (P2) A cache database to reduce latency, bypass qps limit and reduce fees if any.
* (P3) Purchase historical data in batch and load into a self hosted database.

## (P1) Algorithm

* (P1) Evaludator. Given concreate data, calculate gains and losses.
* (P1) Simple rules. eg. loss stop, sell at given price, etc
* (P3) Platform statistics gathering. successful rate, order exec delay, e2e latency. 
* (P3) Tax consideration.
* (P4) Given signal, predict future prices.

## Executor

* (P1) General interface to execute buying and selling decisions.
* (P1) Simulate executor. Record execution decision to operate on fake money.
* (P2) Bring in the first platform (to be choosen).
* (P3) Adding more.

## (P2) Visualization

* (P2) Chart graph to show price trend
* (P2) Multi-platform dashboard
* (P2) Execution dashboard

## Testing

* Add tests as we go.
* Should not slow down development.
