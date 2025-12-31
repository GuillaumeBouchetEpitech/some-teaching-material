
build_mode=release
# build_mode=debug

#

LOG_INFO= '[$(build_mode)]'

#

DIR_SRC=						./src

DIR_APPLICATION=		./bin
NAME_APPLICATION=		$(DIR_APPLICATION)/exec

#### DIRS

#### /DIRS


DIR_OBJ=	./obj/small-project-$(build_mode)


#### SRC


# common src
SRC+= \
	$(wildcard \
		$(DIR_SRC)/*.cpp \
		$(DIR_SRC)/abstract-part/*.cpp \
		$(DIR_SRC)/abstract-part/internals/*.cpp \
	)

#

OBJ=		$(patsubst %.cpp, $(DIR_OBJ)/%.o, $(SRC))

#

#######


ifeq ($(build_mode),release)

BUILD_FLAG= -O3

else

BUILD_FLAG= -g3

endif

CXXFLAGS += $(BUILD_FLAG)
CXXFLAGS += -std=c++20
CXXFLAGS += -Wall -W -Wextra -Wunused -Wpedantic -Wshadow -Wconversion -Werror
CXXFLAGS += -I$(DIR_SRC)

CXX=clang++
AR=ar

RM=			rm -rf


#######

#
## RULE(S)

all:	application

ensurefolders:
	@mkdir -p `dirname $(NAME_APPLICATION)`

application:	ensurefolders $(OBJ)
	@echo ' ---> building $(LOG_INFO) "application"'
	@$(CXX) $(CXXFLAGS) $(OBJ) -o $(NAME_APPLICATION) $(LDFLAGS)
	@echo '   --> built $(LOG_INFO) "application"'

#

# for every ".cpp" file
# => ensure the "obj" folder(s)
# => compile in a ".o" file
$(DIR_OBJ)/%.o: %.cpp
	@mkdir -p $(dir $@)
	@echo ' --> processing $(LOG_INFO):' $<
	@$(CXX) -c $(CXXFLAGS) -MMD -MT "$@" -MF "$@.dep" -o "$@" $<

include $(shell test -d $(DIR_OBJ) && find $(DIR_OBJ) -name "*.dep")

#

clean:
	@echo ' -> cleaning $(LOG_INFO): application build file(s)'
	@$(RM) $(DIR_OBJ)
	@echo '   -> cleaned $(LOG_INFO): application build file(s)'

fclean:	clean
	@echo ' -> cleaned $(LOG_INFO): application file(s)'
	@$(RM) $(NAME_APPLICATION)
	@echo '   -> cleaned $(LOG_INFO): application file(s)'

re:			fclean all

.PHONY:	\
	all \
	ensurefolders \
	application \
	clean \
	fclean \
	re

## RULE(S)
#
