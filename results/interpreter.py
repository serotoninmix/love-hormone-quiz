import math

class HormoneResultInterpreter:

    def __init__(self, user_scores):
        self.user_scores = user_scores
        total_score = sum(self.user_scores.values())
        self.overall_score = round((total_score / 45) * 10)
        self.overall_interpretation = self.get_overall_interpretation()
        self.hormone_interpretations = self.interpret_hormone_results()


    def scale_score(self, score):
        return (score / 5) * 10

    def get_overall_level(self, overall_score):
        if overall_score <= 2:
            return 'Very Low'
        elif 2 < overall_score <= 4:
            return 'Low'
        elif 4 < overall_score <= 6:
            return 'Medium'
        elif 6 < overall_score <= 8:
            return 'High'
        else:  # overall_score > 8
            return 'Very High'


    def get_overall_interpretation(self):
        level = self.get_overall_level(self.overall_score)
        overall_interpretations = {
            'Very Low': "This level may suggest a need to nurture and enhance your emotional landscape and relational bonds. Gentle self-care practices, mindfulness, and fostering meaningful connections can help awaken the positive influences of this hormone in your life.",
            'Low': "A hint of potential lies ahead, as this range offers a pathway to deepen your well-being and enrich your relationships. Embracing activities that uplift your spirit and strengthen your bonds with others can illuminate this path of growth and fulfillment.",
            'Medium': "Your results reflect a beneficial level of hormonal influence, nurturing your mood and enriching your relationships. Continuing to cultivate supportive habits and emotional resilience will sustain this positive impact, fostering a sense of well-being and connectedness.",
            'High': "With strong hormonal support, you experience a vibrant drive and rewarding relationships. This is a gift to cherish, yet staying attuned to maintaining equilibrium will ensure these benefits continue to uplift rather than overwhelm.",
            'Very High': "Your journey is marked by intense hormonal influences, brimming with potential yet requiring careful navigation. Mindfulness and balance are your allies, helping you channel this vibrant energy positively while honoring your well-being and relational harmony."
        }
        return {'level': level, 'interpretation': overall_interpretations.get(level)}
    
    def get_detailed_feedback(self, level):
        feedback = {
            'Very Low': {
                'Understanding': "Your results indicate a very low level, which might mean there are untapped opportunities for you to harness the positive effects associated with this hormone. It's a starting point to understand and improve your well-being.",
                'Actionable Steps': "Consider exploring activities that naturally boost this hormone, such as engaging in meaningful social interactions, enjoying nature, or practicing mindfulness. Small, consistent steps can lead to significant changes.",
                'Encouragement': "Remember, every journey begins with a single step. Viewing this score as a starting point for growth can be incredibly empowering. Embrace the journey of personal development with curiosity and compassion for yourself."
            },
            'Low': {
                'Understanding': "A low score suggests there's room to enhance your experience and benefit more from the hormone's positive aspects. It's an invitation to deepen your understanding and connection.",
                'Actionable Steps': "Reflect on daily habits or routines you might adjust to support your well-being. Engaging in activities that bring you joy and connection can be particularly beneficial.",
                'Encouragement': "You're capable of growth and change. Embrace this opportunity to explore new avenues that can enhance your emotional well-being and enrich your relationships."
            },
            'Medium': {
                'Understanding': "This is a good level, indicating that the hormone's positive aspects are actively supporting your mood and relationship dynamics.",
                'Actionable Steps': "Continue nurturing your well-being with consistent self-care practices. Reflect on what's working well and how you can sustain these positive patterns.",
                'Encouragement': "You're doing well in harnessing the benefits of this hormone. Keep building on this foundation, and remember to celebrate your progress and resilience."        
            },
            'High': {
                'Understanding': "Your high score signifies strong hormonal influence, which can be a powerful ally in driving your personal and relational fulfillment.",
                'Actionable Steps': "While embracing the strengths, be mindful of maintaining balance. Too much of a good thing can have its challenges, so it's essential to stay attuned to your emotional landscape.",
                'Encouragement': "You're experiencing the robust benefits of this hormone, enhancing your well-being and connections. Continue to cultivate awareness and gratitude for these positive aspects of your life."        
            },
            'Very High': {
                'Understanding': "An intense level like yours can offer unique strengths and potential challenges. It's important to harness these energies constructively while being aware of any areas where they might feel overwhelming.",
                'Actionable Steps': "Consider if there are moments when this intensity feels unbalanced and explore practices that can help modulate these experiences, such as relaxation techniques, grounding activities, or seeking support when needed.",
                'Encouragement': "Your journey involves balancing these intense experiences with nurturing and grounding practices. Trust in your ability to navigate this path with wisdom and grace, utilizing the strengths this hormone brings to your life."        
            },
        }

        return feedback[level]


    def get_hormone_level(self, score):
            # Convert the score from a 0-5 scale to a 0-10 scale.
            scaled_score = (score / 5) * 10

            if scaled_score <= 2:
                return 'Very Low'
            elif 2 < scaled_score <= 4:
                return 'Low'
            elif 4 < scaled_score <= 6:
                return 'Medium'
            elif 6 < scaled_score <= 8:
                return 'High'
            else:  # scaled_score > 8
                return 'Very High'

    # Ensure all other necessary methods are also within the class
    def interpret_hormone_results(self):
        hormone_interpretations = {}
        for hormone, score in self.user_scores.items():
            level = self.get_hormone_level(score)  # Now this should work as expected
            interpretation = self.get_hormone_interpretation(hormone, level)
            hormone_interpretations[hormone] = {
                'level': level,
                'interpretation': interpretation
            }
        return hormone_interpretations

    def get_hormone_interpretation(self, hormone, level):
        hormone_interpretations = {
            'adrenaline': {
                'Very Low': "At this level, you may experience a tendency toward a lack of enthusiasm and drive in relationship dynamics, possibly affecting shared excitement and passion. Engaging more actively in new and stimulating experiences could help you ignite a spark of vitality and connection between you and your partner(s).",
                'Low': "Slightly below the average range, you might find yourself feeling slightly cautious about embracing risks or seeking adventure, favoring a stable and secure environment instead. Introducing occasional exciting activities could breathe new life into your relationships, creating cherished moments of joy and discovery together.",
                'Medium': "Reflecting a moderate balance, you are likely experiencing a balanced level of passion and excitement, yet with room for deeper engagement. Exploring shared interests that elevate the heart rate, like dancing or hiking, can strengthen bonds and intensify emotional and physical connection.",
                'High': "Signifying heightened sensitivity to excitement and adventure, you may feel an increased draw to thrilling experiences, which can add a vibrant energy to your relationships. It's important to navigate this excitement thoughtfully to avoid potential pitfalls, ensuring that your adventurous spirit enriches rather than complicates your connections.",
                'Very High': "At this heightened level, your desire for excitement and intensity is at its peak, which might lead to impulsiveness or misunderstandings. Fostering open dialogue and understanding within your relationships can help you harness this energy positively, ensuring it strengthens rather than challenges your bonds."
            },
            'dopamine': {
                'Very Low': "At this level, you might experience a notable lack of enthusiasm or motivation toward romantic engagement, possibly affecting the depth of connection and interaction. Cultivating activities that you and your partner(s) find joyous and fulfilling can stimulate dopamine production, enhancing emotional and romantic engagement.",
                'Low': "Slightly below the average, you may feel a gentle ebb in the waves of pleasure and attraction that knit you together with your partner. Finding new or forgotten activities that both of you enjoy can reignite the spark, reinforcing their emotional bond and mutual attraction.",
                'Medium': "At this balanced juncture, your relationship thrives with satisfactory engagement and happiness. To nurture this state, continue to share and cherish adventures and moments, further solidifying your connection and shared joy, enriching the partnership with sustained happiness and mutual growth.",
                'High': "You're likely to feel a heightened sense of pleasure and connectedness, signifying a thriving bond. To harmonize this intensity, integrating thoughtful contemplation and mutual understanding can ensure these potent feelings fortify rather than disrupt your bond - enhance rather than overwhelm the partnership.",
                'Very High': "Experiencing an apex of emotional and motivational intensity can be thrilling, yet it demands careful navigation. Open and sincere communication, coupled with shared goal-setting, can channel this dynamic energy, fostering a profound and satisfying union."
            },
            'endorphins': {
                'Very Low': "This level might reflect challenges in fully experiencing joy and connection within your relationship(s). Introducing activities that foster laughter and enjoyment, such as comedic viewing or playful interactions, can enhance the release of endorphins, boosting your relational contentment.",
                'Low': "You could be sensing a need for more warmth and shared experiences. Incorporating regular, comforting rituals, such as evening walks or cooking together, can foster warmth and closeness, nurturing the emotional bond.",
                'Medium': "Indicative of a healthy level of pleasure and connection, maintaining and building on this through continued shared positive experiences can deepen the bond. Celebrating small successes together or creating joyful memories can reinforce this positive trajectory.",
                'High': "Reflecting a strong sense of shared happiness and intimacy. Your relationship likely radiates strong shared joy and closeness. To uphold this, fostering positive interactions, consistent communication, mutual support, and shared experiences of laughter and love can continue to enhance your relationship's strength and depth.",
                'Very High': "With such intense joy and connection, maintaining awareness and balance is vital to prevent overwhelming intensity. Engaging in candid discussions about each other's emotions and experiences can help sustain a grounded and satisfying relationship. The intensity of connection and joy is profound but should be balanced with mindfulness to ensure it enriches rather than overwhelms."
            },
            'estrogen': {
                'Very Low': "You may find it challenging to deeply connect or communicate effectively in your relationships. Focusing on nurturing activities like sharing personal experiences and supporting each other can enhance connection and empathy among you and your partners.",
                'Low': "A low score suggests there may be room to enhance emotional attunement and nurturing behaviors. Engaging in empathetic listening and expressing understanding and care in daily interactions can help foster a warmer, more connected relationship environment.",
                'Medium': "This indicates a good balance of empathy, communication, and care, suggesting a solid emotional foundation in your relationships. Regular, meaningful interactions can deepen and enrich these connections.",
                'High': "High levels reflect significant emotional connectivity and supportiveness are evident, essential for strong partnerships. Continual empathetic engagement, open communication, and care are key to maintaining vibrant and connected relationships.",
                'Very High': "At this level, while deep emotional connection and empathy is profound, it's important to maintain balance and ensure that the nurturing behavior remains supportive rather than overbearing. Establishing healthy boundaries and encouraging mutual growth can help maintain a balanced and thriving relationship."
            },
            'norepinephrine': {
                'Very Low': "You might be feeling a lack of vitality and passion in your relationships, which can be addressed by trying out new and exciting activities together or engaging in lively discussions to spark mutual enthusiasm, such as trying new experiences together or engaging in stimulating conversations.",
                'Low': "A slightly higher yet low level suggests that you may need a bit more excitement and engagement. Focusing on shared interests that elevate your energy and connection can be beneficial. Consider engaging in activities that both find thrilling or invigorating to boost this dynamic aspect.",
                'Medium': "With medium levels, there is likely a good balance of alertness and energy within the relationship. Maintaining this balance involves nurturing the existing enthusiasm and attentiveness while being mindful of each other's comfort levels with excitement and risk.",
                'High': "High levels suggest there's considerable passion and energy in your interactions, which is great! Just make sure to channel this energy positively and maintain a supportive environment to mitigate any potential stress. Focus on cultivating understanding, empathy, and patience to balance the high energy and mitigate any potential stress or conflicts.",
                'Very High': "At very high levels, the intensity of feelings and actions can be overwhelming, potentially leading to strain in the relationship. It's important to find ways to calm and ground the relationship dynamics. Practicing relaxation techniques, mindfulness, or engaging in calm, bonding activities can help balance the heightened state and foster deeper, more stable connections."
            },
            'oxytocin': {
                'Very Low': "At this level, there may be a significant challenge in feeling connected and bonded with your partner(s). It's vital to foster environments that encourage trust and affection, such as sharing meaningful experiences and expressing appreciation and gratitude to enhance your emotional bond(s).",
                'Low': "Slightly higher but still low, this level suggests a need to deepen trust and empathy in your relationship(s). Engaging in activities that promote mutual understanding and support, like deep conversations or couples' therapy, can be beneficial in strengthening your connection.",
                'Medium': "You likely experience a good sense of connection and trust in your relationship(s). Maintaining this involves continuing practices that nurture your bond, like consistent communication, shared laughter, and supportive actions, ensuring the relationship continues to thrive.",
                'High': "High levels indicate strong affection, trust, and empathy within your relationship(s). To sustain these positive dynamics, focus on reciprocal understanding and respect for each other's needs and boundaries. Celebrate your strong connections while staying mindful of maintaining a healthy balance of closeness and individuality.",
                'Very High': "At the highest level, while your bond(s) might seem exceptionally strong, there's a risk of becoming overly dependent or enmeshed. Ensuring that you and your partner(s) maintain their individuality, pursuing personal interests alongside shared activities, can prevent potential issues with over-attachment or jealousy and maintain a healthy, balanced relationship."
            },
            'serotonin': {
                'Very Low': "This level may indicate significant challenges in maintaining a stable mood, possibly affecting emotional connections in your relationship(s). It's crucial to explore activities or therapies that enhance well-being and emotional regulation, fostering a more supportive and understanding relationship environment.",
                'Low': "Slightly above very low, this level still suggests difficulties with mood stability and emotional balance. Engaging in practices that promote relaxation and happiness, such as exercise, mindfulness, or hobbies, can help improve your overall mood and positively impact your relationship dynamics.",
                'Medium': "With serotonin levels above average, you likely experience a generally positive mood and emotional resilience. Maintaining this state involves continued engagement in activities that foster well-being, open communication, and shared positive experiences, contributing to a fulfilling and harmonious relationship.",
                'High': "High levels suggest a strong foundation of mood stability, self-esteem, and emotional balance, greatly benefiting relational satisfaction. To sustain these benefits, focus on nurturing your relationship(s) through empathetic listening, mutual appreciation, and ongoing personal growth to deepen the connection with your partner(s).",
                'Very High': "At the highest levels, while overall mood and relationship satisfaction might be exceptionally positive, it's important to stay grounded and attentive to your partners' needs. Ensure that open communication and emotional attunement are maintained, preventing complacency and fostering a dynamic and responsive relationship."
            },
            'testosterone': {
                'Very Low': "This may suggest challenges in experiencing strong sexual desire and assertiveness, which could impact the dynamics of your romantic relationships. Encouraging open communication about needs and desires, coupled with activities that boost self-esteem, may help enhance intimacy and partnership.",
                'Low': "Slightly higher yet below the average range, this level might indicate modest difficulties in assertiveness and sexual drive. Engaging in healthy lifestyle choices, such as regular exercise and stress management, can aid in boosting testosterone levels and enhancing relationship satisfaction.",
                'Medium': "You likely exhibit a good balance of confidence and assertiveness, contributing positively to your relationships. Maintaining this balance involves continued focus on respectful communication, shared adventures, and mutual understanding to keep your relationship(s) vibrant and fulfilling.",
                'High': "High levels indicate strong sexual desire, assertiveness, and potentially competitive behavior. While these can enrich a relationship, ensuring that they are balanced with empathy, respect, and cooperative partnership is vital to prevent conflicts and deepen the bond.",
                'Very High': "At the highest spectrum, while passion and self-assurance may be pronounced, they could lead to excessive dominance or aggression. Balancing these traits with active listening, compassion, and valuing your partner's perspective is crucial to nurturing a supportive and loving relationship."
            },
            'vasopressin': {
                'Very Low': "This may indicate challenges in forming deep emotional bonds and a tendency toward less traditional bonding in relationships. Encouraging activities that promote closeness and trust, such as sharing intimate conversations or experiences, may help enhance emotional connections and partnership security.",
                'Low': "These levels suggest a modest struggle in fully embracing trust and deep bonding in relationships. Engaging in trust-building exercises and open communication can foster a stronger sense of security and connection with your partner.",
                'Medium': "Individuals at this level tend to exhibit healthy bonding behaviors, showing balanced protectiveness and commitment. Maintaining this through ongoing affectionate gestures and reassurances of commitment can continue to nurture the relationship's growth and depth.",
                'High': "Higher levels indicate strong pair bonding tendencies and a clear inclination toward monogamy and trust. While these qualities can enrich a relationship, it's important to balance them with respect for personal space and individuality, ensuring a healthy, supportive partnership.",
                'Very High': "At the peak range, while loyalty and protectiveness are pronounced, they may verge into overprotectiveness or excessive control. Balancing strong bonding desires with fostering a supportive, open environment allows both partners to feel secure yet free within the relationship."
            }
        }

        return hormone_interpretations[hormone].get(level, "Interpretation not available.")
    
    def get_hormone_definitions(self):
        return {
            'adrenaline': "Adrenaline, also known as epinephrine, is a hormone and neurotransmitter involved in the body's fight-or-flight response. It boosts energy, increases heart rate, and raises blood pressure, preparing the body to react quickly to stressful situations. In relationships, adrenaline can heighten emotions, contributing to intense connections or conflicts.",
            'dopamine': "Dopamine is a neurotransmitter that plays a key role in the brain's reward system, associated with pleasure, motivation, and learning. It influences romantic attraction, desire, and love, enhancing feelings of enjoyment and reinforcing rewarding relationship experiences.",
            'endorphins': "Endorphins are neurotransmitters that act as natural painkillers and mood elevators. They promote feelings of well-being and can enhance pleasure and satisfaction in relationships. Endorphins are released during physical intimacy, laughter, and shared activities, fostering connection and closeness.",
            'estrogen': "Estrogen is a primary female sex hormone that plays a crucial role in reproductive and sexual health, mood regulation, and social behavior. In relationships, estrogen influences emotional responsiveness, attachment, and conflict resolution, contributing to relationship satisfaction and stability.",
            'norepinephrine': "Norepinephrine, similar to adrenaline, functions as both a hormone and neurotransmitter. It is involved in arousal, alertness, and the stress response. In romantic contexts, norepinephrine can intensify feelings of love and attachment while also influencing stress and conflict in relationships.",
            'oxytocin': "Often termed the love hormone, oxytocin is pivotal in facilitating social bonds, trust, and empathy. It strengthens attachment, promotes intimacy, and enhances partner supportiveness, playing a key role in relationship development and maintenance.",
            'serotonin': "Serotonin regulates mood, appetite, and sleep, with significant implications for emotional well-being and social behavior. It affects how individuals perceive and respond to relationship experiences, influencing happiness, anxiety, and conflict resolution.",
            'testosterone': "While commonly associated with male sexuality and aggression, testosterone affects both genders, influencing sexual desire, competitiveness, and dominance. In relationships, it can impact attraction, sexual activity, and even partner selection.",
            'vasopressin': "Vasopressin is closely linked to water regulation in the body but also plays a role in social behavior, particularly in males. It supports pair-bonding, paternal responses, and partner protection, influencing long-term relationship commitment and fidelity."
        }