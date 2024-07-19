# Pyliven
Pronounced /ˈpaɪlʌɪvɛn/

Pyliven is an initiative to add stateful computation in the Python programming language. With this package, your python variables with automatically update if a dependency variable is updated. It's a new way to calculate in python.

## Use
Pyliven can be leveraged in multiple ways. One use-case can be to write formulae in python. Let's try with the classic Electrostatic force formula:
```python
from pyliven.liven import LiveNum

k = 9e9
q1 = LiveNum(2e-3)
q2 = LiveNum(3e-3)

r = LiveNum(1)

Force = k*q1*q2/r**2
```
Now we can directly update any of `q1`, `q2`, and `r`, and the value of `Force` will update.
```python
r.update(5)
print(Force)
```

You can find the complete documentation at [https://keymii.github.io/pyliven](https://keymii.github.io/pyliven)