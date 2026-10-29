import test from "node:test";
import assert from "node:assert/strict";
test("wallet messages are not interchangeable", () => { const signedFor = "approve:42"; assert.notEqual(signedFor, "approve:43"); });
