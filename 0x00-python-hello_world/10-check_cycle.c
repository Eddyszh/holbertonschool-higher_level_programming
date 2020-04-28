#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to struct
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list, *next = list;

	if (!list)
		return (0);
	while (temp->next && next->next->next)
	{
		temp = temp->next;
		next = next->next->next;
		if (temp == next)
			return (1);
	}
	return (0);
}
