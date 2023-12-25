#include <Python.h>

static PyObject *hash_password(PyObject *self, PyObject *args) {
    char key[] = "thisisthekey";
    char *pass;
    size_t pass_len;
    size_t key_len;

    if (!PyArg_ParseTuple(args, "s", &pass)) {
        NULL;
    }
    pass_len = strlen(pass);
    key_len = strlen(key);

    char *hashed = (char *)malloc(pass_len + 1);
    for (size_t i = 0; i < pass_len; i++) {
        hashed[i] = pass[i] ^ key[i % key_len];
    }
    hashed[pass_len] = '\0';

    return Py_BuildValue("s", hashed);
}

static PyObject *check_password(PyObject *self, PyObject *args) {
    char* pass;
    char* hash;
    char key[] = "thisisthekey";
    size_t pass_len;
    size_t key_len;
    int result = 1;

    if (!PyArg_ParseTuple(args, "ss", &pass, &hash)) {
        NULL;
    }
    pass_len = strlen(pass);
    key_len = strlen(key);

    char *hashed_pass = (char *)malloc(pass_len + 1);
    for (size_t i = 0; i < pass_len; i++) {
        hashed_pass[i] = pass[i] ^ key[i % key_len];
    }
    hashed_pass[pass_len] = '\0';
    result = strcmp(hash, hashed_pass);
    free(hashed_pass);

    return Py_BuildValue("i", result);
}

static PyMethodDef hash_funcs[] = {
   {"hash_password", (PyCFunction)hash_password, METH_VARARGS, "Hash password"},
   {"check_password", (PyCFunction)check_password, METH_VARARGS, "Check password"},
   {NULL}
};

static PyModuleDef hash_module = {
    PyModuleDef_HEAD_INIT,
    "hash",
    "Extension module hash",
    0,
    hash_funcs
};

void PyInit_hash(void) {
   PyModule_Create(&hash_module);
}

