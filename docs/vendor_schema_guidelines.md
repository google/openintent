# Vendor Schema Guidelines

While the project hopes to cover any and all requirements from a vendor neutral
data perspective, there will come times that a vendor wants to include something
that is specific to their product, or wants to include something that doesn't
belong or fall into the scope of OpenIntent.

After much discussion, we decided to take a neutral stance in that we don't care
if you want to put extra information into an OpenIntent payload or not. The only
concern we have, is about current or future schema collision with non-OpenIntent
data.

## Example of Schema Collision
An example of schema collisions would be the following:

Steve's Wifi Planner adds key `id` to an access_point object inside the
OpenIntent payloads it produces.  For Steve's Wifi Planner, it uses ids as
integers.

In the future, the OpenIntent schema adds `id` as to the access_point,
but defines them as an OID that looks like
`cff3ceaefc955f0dbe1957017db181bc49913781`

Now there becomes confusion for those who were using Steve's `id` and if those
requirements align with what is now defined in the standard.

## Avoiding Schema Collisions

To avoid this, the recommendation is to append your product or vendor name to
the beginning of your key.  this way humans can tell this is unique to your
product, as well as they can be safely ignore by most jsonschema parsers.

Example:

```json
"steve_id": 000001,
"steveswifiplanner_id": 000002
```
Neither of these would collide with:
```json
"id": "cff3ceaefc955f0dbe1957017db181bc49913781"
```


## Recommendations

I would recommend that you use something that is very specific to your product/
company to reduce the chances of it colliding with someone elses.

Examples:
- using `meraki_` instead of `m_`, as `m_` could be confused with Mist.
- use `haminaplanner` instead of `planner`


You could also append multiple words with underscores as long as the prefix to
the vendor proprietary information is descriptive and is unique to your company.

Example
- `hamina_planner_id`
- `eino_ai_id`


Leveraging this ensures that the OpenIntent schema isn't impacted by
out-of-schema information as well as ensures that vendors have the freedom to
include the data they want.
