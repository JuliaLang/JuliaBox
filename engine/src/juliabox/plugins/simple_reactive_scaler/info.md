## Simple Reactive Scaler

Add instances based on load.  The number of instances to add at different thresholds can be specified under `scaler_config` in `cloud_host` in `jbox.user`.  For example,

```python
'cloud_host': {
    ...,
	'scaler_config': {
	    60: 1,
		70: 2,
		80: 3,
	}
}
```

If the average load is between 60 and 70 percent, 1 instance will be added.  If the average load is between 70 and 80 percent, 2 instances will be added.  If the average load is greater than 80 percent 3 instances will be added.
