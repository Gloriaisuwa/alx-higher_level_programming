#include "lists.h"

/**
 * check_cycle - function that checks if a list has a cycle
 * @list: linked list
 * Return: 1 if there is a cycle and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);
	fast = list->next;
	slow = list;

	while ( slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
