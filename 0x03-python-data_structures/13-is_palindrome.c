#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to struct
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);
	return (look_palin(head, *head));
}

/**
 * look_palin - looks for the palindrome
 * @head: pointer to head
 * @tail: pointer to tail
 * Return: 1 if is palindrome
 */
int look_palin(listint_t **head, listint_t *tail)
{
	if (!tail)
		return (1);
	if (look_palin(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
