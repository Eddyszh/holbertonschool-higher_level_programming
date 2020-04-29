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
	listint_t *temp = *head;
	listint_t *new;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	while (temp->next != NULL && new->n > temp->next->n)
		temp = temp->next;
	new->next = temp->next;
	temp->next = new;
	while (temp->next != NULL)
		temp = temp->next;
	return (new);
}
