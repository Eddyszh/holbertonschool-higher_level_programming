#include <stdlib.h>
#include "lists.h"
/**
 * listint_t *insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to struct
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cpy = *head;
	listint_t *new, *temp;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	else
	{
		while (cpy && number > cpy->n)
		{
			temp = cpy;
			cpy = cpy->next;
		}
		temp->next = new;
		new->next = cpy;
	}
	return (new);
}
