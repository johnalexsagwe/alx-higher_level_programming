#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle.
 * @list: A pointer to the head of the linked list to check.
 *
 * Return: 1 if the linked list has a cycle, 0 if it doesn't.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;/* Initialize a slow pointer to the beginning of the list */
	listint_t *fast = list;/* Initialize a fast pointer to the beginning of the list. */

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
