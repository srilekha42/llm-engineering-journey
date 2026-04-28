### ✅ Day 3: Controlling LLM Output (Very Important)

#### 🔹 What I Learned (Simple)

* LLM output is **not reliable by default**
* Even if we ask for JSON, it may:

  * break format ❌
  * add extra text ❌
  * change structure ❌

👉 So we must **control and verify output**

---

#### 🔹 New Concepts

**1. Structured Output**

* Instead of normal text → force LLM to return JSON
* Helps in using output in real applications

---

**2. Parsing**

* LLM gives output as **string**
* We convert it into usable format using:

```python
json.loads(output)
```

👉 This is called **parsing**

---

**3. Why Parsing Fails**

* Invalid JSON (missing quotes, commas)
* Extra text like:

  * "Here is your answer"
  * ```json blocks
    ```

---

**4. Validation**

* Even if JSON is valid → it can be wrong
* Example:

  * empty fields
  * missing key points
  * wrong structure

👉 So we check output before using it

---

**5. Retry Mechanism**

* If JSON is broken → ask LLM to fix it
* If output is weak → ask LLM to improve

---

**6. Schema Problems**

* Expected:

  ```json
  ["point1", "point2"]
  ```

* Got:

  ```json
  [{"name": "..."}]
  ```

👉 LLM may change structure → must handle it

---

#### 🔹 Key Learning

> LLM output is probabilistic (not guaranteed)

So we must:

* parse ✔️
* validate ✔️
* retry ✔️

---

#### 🔹 Final Understanding

LLM pipeline:

```text
Input → LLM → Extract → Parse → Validate → Fix → Improve
```

---

#### 🔹 Big Insight

> Using LLM is easy
> Controlling LLM is real engineering
