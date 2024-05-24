import numpy as np

def bayes_theorem(p_a, p_b_given_a, p_b):
    return (p_b_given_a * p_a) / p_b

def joint_probability(p_a, p_b_given_a):
    return p_a * p_b_given_a

def conditional_probability(p_a_and_b, p_a):
    return p_a_and_b / p_a

p_disease = 0.01
p_positive_given_disease = 0.9
p_positive_given_no_disease = 0.05
p_no_disease = 1 - p_disease

p_positive = (p_positive_given_disease * p_disease) + (p_positive_given_no_disease * p_no_disease)
p_disease_given_positive = bayes_theorem(p_disease, p_positive_given_disease, p_positive)
print("Probability of having the disease given a positive test result:", p_disease_given_positive)

p_red_cards = 26 / 52
p_face_cards_given_red = 6 / 26
p_red_and_face = joint_probability(p_red_cards, p_face_cards_given_red)
print("Joint probability of drawing a red card and a face card:", p_red_and_face)

p_red_cards = 26 / 52
p_face_cards_given_red = 6 / 26
p_face_given_red = conditional_probability(p_face_cards_given_red, p_red_cards)
print("Conditional probability of drawing a face card given the card drawn is red:", p_face_given_red)
