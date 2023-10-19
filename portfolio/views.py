from rest_framework.viewsets import ReadOnlyModelViewSet
from portfolio.models import Portfolio, PostLike, PortfolioCategory
from portfolio.serializers import PortfolioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class PortfolioView(ReadOnlyModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        obj = self.get_object()
        obj.watches += 1
        obj.save()
        return response

    @action(detail=True, methods=['GET'])
    def like(self, request, pk=None):
        ip_add = request.META.get('HTTP_X_REAL_IP')
        # ip_add = request.META.get('REMOTE_ADDR')  # Ozgartirish estan chiqmasin
        print(ip_add)
        portfolio_obj = self.get_object()
        obj = PostLike.objects.filter(ip_address=ip_add)
        if len(obj) == 0:
            PostLike.objects.create(
                post_id=portfolio_obj.id,
                ip_address=ip_add
            )
            portfolio_obj.like += 1
            portfolio_obj.save()
            return Response(status=status.HTTP_201_CREATED)
        obj.delete()
        portfolio_obj.like -= 1
        portfolio_obj.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def category_ids(self, request, pk=None):
        try:
            category = PortfolioCategory.objects.get(pk=pk)
        except PortfolioCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        portfolios = Portfolio.objects.filter(category=category)

        serializer = PortfolioSerializer(portfolios, many=True, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)
