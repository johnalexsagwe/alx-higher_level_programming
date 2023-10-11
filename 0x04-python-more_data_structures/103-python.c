#include <stdio.h>
#include <Python.h>

void print_py_bytes(PyObject *p);

/**
* print_py_list - prints some basic info about Python lists
*
* @p: Python object
*
* Return: No Return
*/
void print_py_list(PyObject *p)
{
long int i, size, alloc;
PyObject *item;

size = PyList_Size(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Python list info\n");

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (i = 0; i < size; i++)
{
item = PyList_GET_ITEM(p, i);
printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
if (PyBytes_Check(item))
print_py_bytes(item);
}
}

/**
* print_py_bytes - prints some basic info about Python bytes objects
*
* @p: Python object
*
* Return: No Return
*/
void print_py_bytes(PyObject *p)
{
long int i, size;
char *data;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
data = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", data);

if (size < 10)
printf("  first %ld bytes:", size + 1);
else
printf("  first 10 bytes:"), size = 9;

for (i = 0; i <= size; i++)
if (data[i])
printf(" %02hhx", data[i]);
else
printf(" 00");
printf("\n");
}
