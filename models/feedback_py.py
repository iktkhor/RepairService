class Feedback:
    """Класс отзыва"""

    def __init__(self, fb_id, order_id, fb_rating, fb_text):
        self.feedback_id = fb_id
        self.order_id = order_id
        self.feedback_rating = fb_rating
        self.feedback_text = fb_text
